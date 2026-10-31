export default {
  expo: {
    name: 'أشبال الإسلام',
    slug: 'ashbal-islam',
    version: '1.0.0',
    orientation: 'portrait',
    icon: './assets/icon.png',
    userInterfaceStyle: 'light',
    scheme: 'ashbal',
    splash: {
      image: './assets/splash.png',
      resizeMode: 'contain',
      backgroundColor: '#ffffff',
    },
    ios: {
      supportsTablet: true,
      bundleIdentifier: 'com.ashbalislam.app',
    },
    android: {
      adaptiveIcon: {
        foregroundImage: './assets/adaptive-icon.png',
        backgroundColor: '#ffffff',
      },
      package: 'com.ashbalislam.app',
      permissions: ['INTERNET', 'ACCESS_NETWORK_STATE'],
    },
  },
};
