import firebase from 'firebase'

export default {
    state: {
        user: {
            isAuthentificated: false,
            uid: null
        }
    },
    mutations: {

    },
    actions: {
        SIGNUP(payload) {
            firebase.auth().createUserWithEmailAndPassword(payload.email, payload.password)
            .then(user => {
                console.log(user)
            })
            .catch(function (error) {
                console.log(error)
            });
        }
    }
}