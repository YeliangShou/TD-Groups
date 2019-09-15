const functions = require('firebase-functions');
const admin = require('firebase-admin');
const Firestore = require('@google-cloud/firestore');

const PROJECTID = 'td-groups';

const firestore = new Firestore({
    projectId: PROJECTID,
});

admin.initializeApp();

exports.addNewUser = functions.auth.user().onCreate(async (user) => {
    try {
        var setDoc = firestore.collection('users').doc(user.uid).set({
            'emailId' : user.email, 'name': user.displayName, 'td-customer-id' : "", "groups" : []});
        
        console.log(`Added user with uid ${user.uid} to the database`);
        return setDoc;
    } catch (error) {
        console.log(`There was an error adding the new user with uid ${user.uid} to the database:`, error);
	return null;
    }
});

exports.deleteUser = functions.auth.user().onDelete(async (user) => {
    try {
        var deleteDoc = await firestore.collection('users').doc(user.uid).delete();
        console.log(`Deleted user with uid ${user.uid} from the database.`);
        return deleteDoc;
    } catch (error) {
        console.log(`There was an error deleting the user with uid ${user.uid} from the database:`, error);
	return null
    }
});
