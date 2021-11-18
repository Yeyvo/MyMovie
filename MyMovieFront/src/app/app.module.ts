import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import {HeaderComponent} from './header/header.component';
import {SignupComponent} from './auth/signup/signup.component';
import {SigninComponent} from './auth/signin/signin.component';
import {ProfileComponent} from './profile/profile.component';
import {HomeComponent} from './home/home.component';
import {AuthService} from "./services/auth.service";
import {MoviesService} from "./services/movies.service";
import { FourOhFourComponent } from './four-oh-four/four-oh-four.component';
import {RouterModule, Routes} from "@angular/router";
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { SliderComponent } from './home/slider/slider.component';
import {AngularFireModule} from "@angular/fire/compat";
import {AngularFirestoreModule} from "@angular/fire/compat/firestore";
import {AngularFireAuthModule} from "@angular/fire/compat/auth";
import { initializeApp,provideFirebaseApp } from '@angular/fire/app';
import { environment } from '../environments/environment';
import { provideAnalytics,getAnalytics,ScreenTrackingService,UserTrackingService } from '@angular/fire/analytics';
import { provideAuth,getAuth } from '@angular/fire/auth';
import { provideDatabase,getDatabase } from '@angular/fire/database';
import { provideFirestore,getFirestore } from '@angular/fire/firestore';
import { provideFunctions,getFunctions } from '@angular/fire/functions';
import { provideMessaging,getMessaging } from '@angular/fire/messaging';
import { providePerformance,getPerformance } from '@angular/fire/performance';
import { provideRemoteConfig,getRemoteConfig } from '@angular/fire/remote-config';
import { provideStorage,getStorage } from '@angular/fire/storage';

const appRoutes: Routes = [
  {path: 'auth/signup', component: SignupComponent},
  {path: 'auth/signin', component: SigninComponent},
  {path: 'auth/profile', component: ProfileComponent},
  // {path: 'movies',/*canActivate:[AuthGuardService], */component: },
  // {path: 'movies/view/:id',/*canActivate:[AuthGuardService], ,*/ component: SingleBookComponent},
  // {path: 'movies/new',/*canActivate:[AuthGuardService], ,*/ component: FormBookComponent},
  {path: '', component:HomeComponent, pathMatch: 'full'},
  {path: 'not-found', component: FourOhFourComponent},
  { path: '**' , redirectTo:'not-found'},
];

const firebaseConfig = {
  apiKey: "AIzaSyB_EBZG7QVI6TXcufOGA7l23VbM-Y9sNIs",
  authDomain: "my-movie-pi.firebaseapp.com",
  projectId: "my-movie-pi",
  storageBucket: "my-movie-pi.appspot.com",
  messagingSenderId: "690751329830",
  appId: "1:690751329830:web:e42cdf9ba5f6096028b8e7",
  measurementId: "G-69M7TMBY6P",
  databaseURL:"https://my-movie-pi-default-rtdb.europe-west1.firebasedatabase.app/"

};

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    SignupComponent,
    SigninComponent,
    ProfileComponent,
    HomeComponent,
    FourOhFourComponent,
    SliderComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    NgbModule,
    RouterModule.forRoot(appRoutes),
    FontAwesomeModule,
    AngularFireModule.initializeApp(firebaseConfig),
    AngularFirestoreModule,
    AngularFireAuthModule,
    provideFirebaseApp(() => initializeApp(environment.firebase)),
    // provideAnalytics(() => getAnalytics()),
    provideAuth(() => getAuth()),
    ReactiveFormsModule,
    // provideDatabase(() => getDatabase()),
    // provideFirestore(() => getFirestore()),
    // provideFunctions(() => getFunctions()),
    // provideMessaging(() => getMessaging()),
    // providePerformance(() => getPerformance()),
    // provideRemoteConfig(() => getRemoteConfig()),
    // provideStorage(() => getStorage()),
  ],
  providers: [AuthService, MoviesService, ScreenTrackingService,UserTrackingService],
  bootstrap: [AppComponent]
})
export class AppModule {
}
