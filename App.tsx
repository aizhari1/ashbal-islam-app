import { useCallback, useEffect, useRef, useState } from 'react'
import {
  ActivityIndicator,
  BackHandler,
  Platform,
  StatusBar,
  StyleSheet,
  View,
  Image,
  Text,
} from 'react-native'
import { WebView } from 'react-native-webview'
import * as SplashScreen from 'expo-splash-screen'
import { StatusBar as ExpoStatusBar } from 'expo-status-bar'

const APP_URL = 'https://ashbal-islam.vercel.app'

SplashScreen.preventAutoHideAsync().catch(() => {})

export default function App() {
  const webRef = useRef<WebView>(null)
  const [canGoBack, setCanGoBack] = useState(false)
  const [loading, setLoading] = useState(true)
  const [boot, setBoot] = useState(true)

  useEffect(() => {
    const t = setTimeout(() => {
      setBoot(false)
      SplashScreen.hideAsync().catch(() => {})
    }, 1200)
    return () => clearTimeout(t)
  }, [])

  useEffect(() => {
    if (Platform.OS !== 'android') return
    const sub = BackHandler.addEventListener('hardwareBackPress', () => {
      if (canGoBack && webRef.current) {
        webRef.current.goBack()
        return true
      }
      return false
    })
    return () => sub.remove()
  }, [canGoBack])

  const onLoadEnd = useCallback(() => {
    setLoading(false)
    SplashScreen.hideAsync().catch(() => {})
  }, [])

  if (boot) {
    return (
      <View style={styles.splash}>
        <Image source={require('./assets/icon.png')} style={styles.logo} resizeMode="contain" />
        <Text style={styles.title}>أكاديمية أشبال الإسلام</Text>
        <Text style={styles.sub}>لتعليم القرآن الكريم وعلومه</Text>
        <ActivityIndicator color="#0B6B3A" style={{ marginTop: 24 }} />
      </View>
    )
  }

  return (
    <View style={styles.root}>
      <ExpoStatusBar style="dark" />
      <StatusBar backgroundColor="#ffffff" barStyle="dark-content" />
      {loading && (
        <View style={styles.loader}>
          <Image source={require('./assets/icon.png')} style={{ width: 72, height: 72 }} />
          <ActivityIndicator color="#0B6B3A" style={{ marginTop: 12 }} />
        </View>
      )}
      <WebView
        ref={webRef}
        source={{ uri: APP_URL }}
        style={styles.web}
        onLoadEnd={onLoadEnd}
        onNavigationStateChange={(nav) => setCanGoBack(nav.canGoBack)}
        startInLoadingState
        javaScriptEnabled
        domStorageEnabled
        sharedCookiesEnabled
        thirdPartyCookiesEnabled
        allowsBackForwardNavigationGestures
        setSupportMultipleWindows={false}
        applicationNameForUserAgent="AshbalIslamApp/1.0"
      />
    </View>
  )
}

const styles = StyleSheet.create({
  root: { flex: 1, backgroundColor: '#ffffff' },
  web: { flex: 1 },
  splash: {
    flex: 1,
    backgroundColor: '#ffffff',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 24,
  },
  logo: { width: 180, height: 180, marginBottom: 16 },
  title: { color: '#0B6B3A', fontSize: 20, fontWeight: '700' },
  sub: { color: '#6f7974', fontSize: 13, marginTop: 6 },
  loader: {
    ...StyleSheet.absoluteFillObject,
    backgroundColor: '#ffffff',
    alignItems: 'center',
    justifyContent: 'center',
    zIndex: 10,
  },
})
