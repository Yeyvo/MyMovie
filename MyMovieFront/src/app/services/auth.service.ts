import {Injectable} from '@angular/core';
import {AngularFireAuth} from "@angular/fire/compat/auth";
import {AngularFirestore, AngularFirestoreDocument} from "@angular/fire/compat/firestore";
import {Router} from "@angular/router";
import {Observable, of, Subject} from "rxjs";
import {User} from "../models/User";
import {first, switchMap} from "rxjs/operators";
import firebase from 'firebase/compat/app';
import {doc} from "@angular/fire/firestore";

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  defaultImageUrl: string = "https://s3.eu-central-1.amazonaws.com/bootstrapbaymisc/blog/24_days_bootstrap/fox.jpg";
  user$: Observable<User >; //database record , user document
  isAuth: boolean = false;

  authSubject : Subject<boolean> = new Subject<boolean>();

  // userDataSubject : Subject<User> = new Subject<User>();
  // user : User;

  constructor(
    private afAuth: AngularFireAuth,
    private afs: AngularFirestore,
    private router: Router
  ) {

    this.user$ = this.afAuth.authState.pipe(
      switchMap(user => {
        if (user) {
          return this.afs.doc<User>(`users/${user.uid}`).valueChanges();
        } else {
          return of(null);
        }
      })
    );

    firebase.auth().onAuthStateChanged((user) => {
      if (user) {
        this.isAuth = true;
        this.emitAuthSubject();
      } else {
        this.isAuth = false;
        this.emitAuthSubject();
      }
    });
  }

  createNewUserEmailPass(username : string , email: string, password: string) {
    return new Promise((resolve, reject) => {
      this.afAuth.createUserWithEmailAndPassword(email, password)
        .then(
          (userCredential) => {
            let userData :  User = {
              uid: userCredential.user.uid,
              email: userCredential.user.email,
              displayName: username,
              photoURL: userCredential.user.photoURL == null ? this.defaultImageUrl : userCredential.user.photoURL
            }
            this.updateUserData(userData)
            resolve(userCredential);
          }
        ).catch((err) => {
        reject(err);
      });

    });

  }

  async googleSignIn() {
    const provider = new firebase.auth.GoogleAuthProvider();
    const credential = await this.afAuth.signInWithPopup(provider);
    // firebase.auth.fetchProvidersForEmail("emailaddress@gmail.com");
    this.router.navigate(['/']);
    return this.updateUserData(credential.user);

  }

  signInUser(email: string, password: string) {
    return new Promise((resolve, reject) => {
      this.afAuth.signInWithEmailAndPassword( email, password).then((val) => {
        resolve(val);
      }).catch((err) => {
        reject(err);
      })
    });
  }

  docExists(path: string) {
    return this.afs.doc(path).valueChanges().pipe(first()).toPromise()
  }

  private async updateUserData(user: any) {
    const userRef: AngularFirestoreDocument<User> = this.afs.doc(`users/${user.uid}`);
    const datafirstTime = {
      uid: user.uid,
      email: user.email,
      displayName: user.displayName,
      photoURL: user.photoURL,
      recommendedMovies: []
    }

    const dataGeneral = {
      uid: user.uid,
      email: user.email,
      photoURL: user.photoURL
    }

    // firebase.auth().fetchSignInMethodsForEmail(user.email)
    //   .then(function(signInMethods) {
    //     if (signInMethods.length === 0) {
    //
    //     } else{
    //
    //     }
    //   })
    const doc = await this.docExists(`users/${user.uid}`);

    if (doc) {
      userRef.set(dataGeneral, {merge: true});
      // this.user = dataGeneral;
    } else {
      userRef.set(datafirstTime, {merge: true});

    }

    // return
  }

  async signOut() {
    await this.afAuth.signOut();
    // await Promise.all([this.afAuth.signOut(), this.emitAppareilSubject()]);
    this.router.navigate(['/']);
  }

  emitAuthSubject() {
    this.authSubject.next(this.isAuth);
  }

  // emitUserDataSubject(){
  //   this.userDataSubject.next(this.)
  // }


  getUserData(){
    // const docRef = doc( `users/${user.uid}`);

  }

  sendResetEmail(email: string) {
    this.afAuth.sendPasswordResetEmail(email).then(r => {
      console.log(" Sent ")
    }).catch(err =>{
      console.log(err);
    });
  }

  async updateData(user: User) {
    return (await this.afAuth.currentUser).updateProfile(user);
  }

}
