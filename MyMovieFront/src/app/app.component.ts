import { Component } from '@angular/core';

import {initializeApp} from "firebase/app";
import {getAnalytics} from "firebase/analytics";
import {getDatabase} from "firebase/database";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'MyMovieFront';
  // model = {
  //   left: true,
  //   middle: false,
  //   right: false
  // };
  constructor(){


// // Initialize Firebase
//     const app = initializeApp(firebaseConfig);
//     const analytics = getAnalytics(app);
//     const db = getDatabase(app);
  }
}
