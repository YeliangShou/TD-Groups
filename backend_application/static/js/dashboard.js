

// Initiate firebase auth.
function initFirebaseAuth() {
  // Listen to auth state changes.
  firebase.auth().onAuthStateChanged(authStateObserver);
}

// Triggers when the auth state change for instance when the user signs-in or signs-out.
function authStateObserver(user) {
  if (!user) { // User is signed in!
    console.log("Sign Out");
    window.location = 'home';
    location.reload(); 
  }
}



const signOutButton = document.getElementById('signOut');

signOutButton.addEventListener("click",
 () => {
   firebase.auth().signOut();
   console.log("sign out");
});


// initialize Firebase
initFirebaseAuth();