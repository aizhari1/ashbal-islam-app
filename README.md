# تطبيق أشبال الإسلام (Android)

تطبيق موبايل حقيقي — أيقونة الشعار + شاشة افتتاحية.

**المستودع:** https://github.com/aizhari1/ashbal-islam-app  
**النظام داخل التطبيق:** https://ashbal-islam.vercel.app

---

## بناء APK من GitHub (موصى به)

1. افتح: https://github.com/aizhari1/ashbal-islam-app/actions
2. اختار **Build Android APK**
3. اضغط **Run workflow** → **Run workflow**
4. بعد ما يخلص (حوالي 10–20 دقيقة) افتح الـ run
5. من أسفل الصفحة حمّل **ashbal-islam-apk**
6. فك الضغط وثبّت ملف `.apk` على الموبايل

> أول مرة: لو فشل البناء، شغّل الـ workflow تاني بعد دقيقة.

---

## بناء APK من جهازك (EAS)

```bash
git clone https://github.com/aizhari1/ashbal-islam-app.git
cd ashbal-islam-app
npm install
npm run generate-assets
npm i -g eas-cli
eas login
eas build -p android --profile preview
```

---

## التطوير

```bash
npm install
npm run generate-assets
npx expo start
```
