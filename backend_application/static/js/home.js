console.log("HI");


// ...
// Initialize the FirebaseUI widget using Firebase
const ui = new firebaseui.auth.AuthUI(firebase.auth());

// ...
// At the bottom

const startRsvpButton = document.getElementById('startRsvp');



// Listen to RSVP button clicks
startRsvpButton.addEventListener("click",
 () => {
   var provider = new firebase.auth.GoogleAuthProvider();
   firebase.auth().signInWithPopup(provider);
});
