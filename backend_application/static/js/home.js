console.log("HI");


// ...
// Initialize the FirebaseUI widget using Firebase
const ui = new firebaseui.auth.AuthUI(firebase.auth());


// Initiate firebase auth.
function initFirebaseAuth() {
  // Listen to auth state changes.
  firebase.auth().onAuthStateChanged(authStateObserver);
}

// Triggers when the auth state change for instance when the user signs-in or signs-out.
function authStateObserver(user) {
  if (user) { // User is signed in!
    console.log("Sign In");
    //window.location = 'dashboard';
  }
}





// ...
// At the bottom

const startRsvpButton = document.getElementById('startRsvp');
const signOutButton = document.getElementById('signOut');


// Listen to RSVP button clicks
startRsvpButton.addEventListener("click",
 () => {
   var provider = new firebase.auth.GoogleAuthProvider();
   provider.setCustomParameters({prompt: 'select_account'});
   firebase.auth().signInWithPopup(provider);
});

// Listen to RSVP button clicks
signOutButton.addEventListener("click",
 () => {
   firebase.auth().signOut();
   console.log("sign out");
});



// initialize Firebase
initFirebaseAuth();
