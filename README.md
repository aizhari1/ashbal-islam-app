# تطبيق أشبال الإسلام (Android / iOS)

تطبيق موبايل **حقيقي** (Expo + React Native) — مش موقع:

- أيقونة الشعار الرسمي على الشاشة الرئيسية
- شاشة افتتاحية بالشعار أول ما تفتح التطبيق
- يعمل كتطبيق مستقل على الموبايل

## تحميل المشروع
```bash
git clone https://github.com/aizhari1/ashbal-islam-app.git
cd ashbal-islam-app
npm install
npm run generate-assets
```

## بناء APK وتثبيته على الموبايل
```bash
npm i -g eas-cli
eas login
eas build -p android --profile preview
```
بعد ما يخلص البناء، Expo هيديك **رابط APK** — حمّله على الموبايل وثبّته.

## التطوير
```bash
npx expo start
```
