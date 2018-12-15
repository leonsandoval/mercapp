var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
       
];

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event){
    event.respondWith(
        caches.match(event.request).then(function(response) {
            if(response) {
                return response;
            }

            return fetch(event.request);
        })
    );
});

importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var config = {
    apiKey: "AIzaSyDAS6XZPTpwA3Rec7YgY-hUUwhsFk7MNZc",
    authDomain: "listacompras-95ed0.firebaseapp.com",
    databaseURL: "https://listacompras-95ed0.firebaseio.com",
    projectId: "listacompras-95ed0",
    storageBucket: "listacompras-95ed0.appspot.com",
    messagingSenderId: "398111472243"
};
firebase.initializeApp(config);


const messaging = firebase.messaging();


messaging.setBackgroundMessageHandler(function (payload) {

    var title = "titulo de la notificacion"
    var options = {
        body: "Cuerpo de la notificacion",
        icon: '/static/core/img/bolsa.png'
    }

   
    return self.registration.showNotification(title, options);
})