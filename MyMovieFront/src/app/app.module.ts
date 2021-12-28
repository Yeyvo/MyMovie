import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import {HeaderComponent} from './component/includes/header/header.component';
import {SignupComponent} from './component/auth/signup/signup.component';
import {SigninComponent} from './component/auth/signin/signin.component';
import {ProfileComponent} from './component/profile/profile.component';
import {AuthService} from "./services/auth.service";
import {MoviesService} from "./services/movies.service";
import {FourOhFourComponent} from './component/four-oh-four/four-oh-four.component';
import {RouterModule, Routes} from "@angular/router";
import {FontAwesomeModule} from '@fortawesome/angular-fontawesome';
import {AngularFireModule} from "@angular/fire/compat";
import {AngularFirestoreModule} from "@angular/fire/compat/firestore";
import {AngularFireAuthModule} from "@angular/fire/compat/auth";
import {initializeApp, provideFirebaseApp} from '@angular/fire/app';
import {environment} from '../environments/environment';
import {provideAnalytics, getAnalytics, ScreenTrackingService, UserTrackingService} from '@angular/fire/analytics';
import {provideAuth, getAuth} from '@angular/fire/auth';
import {provideDatabase, getDatabase} from '@angular/fire/database';
import {provideFirestore, getFirestore} from '@angular/fire/firestore';
import {provideFunctions, getFunctions} from '@angular/fire/functions';
import {provideMessaging, getMessaging} from '@angular/fire/messaging';
import {providePerformance, getPerformance} from '@angular/fire/performance';
import {provideRemoteConfig, getRemoteConfig} from '@angular/fire/remote-config';
import {provideStorage, getStorage} from '@angular/fire/storage';
import {HttpClient, HttpClientModule} from "@angular/common/http";
import {BrowserAnimationsModule} from "@angular/platform-browser/animations";
import {CarouselModule} from "primeng/carousel";
import {SliderComponent} from "./component/slider/slider.component";
import {SidebarModule} from "primeng/sidebar";
import { SkeletonModule } from './shared/skeleton/skeleton.module';
import {HomeComponent} from "./component/home/home.component";
import {FooterComponent} from "./component/includes/footer/footer.component";
import {MatProgressBarModule} from "@angular/material/progress-bar";
import {MatProgressSpinnerModule} from "@angular/material/progress-spinner";
import {PipeModule} from "./pipe/pipe.module";
import {MoviesComponent} from "./component/movies/movies.component";
import {MovieDetailsModule} from "./component/movie-details/movie-details.module";
import {MoviesRoutingModule} from "./component/movies/movies-routing.module";
import {MoviesModule} from "./component/movies/movies.module";
import {GenreModule} from "./component/genre/genre.module";
import {GenreListModule} from "./component/genre-list/genre-list.module";
import {PersonModule} from "./component/person/person.module";
import {WindowRefService} from "./services/windowRef.service";
import {ButtonModule} from "primeng/button";
import { RecommendationComponent } from './component/recommendation/recommendation.component';

// const appRoutes: Routes = [
//   {path: 'auth/signup', component: SignupComponent},
//   {path: 'auth/signin', component: SigninComponent},
//   {path: 'auth/profile', component: ProfileComponent},
//   {path: '', component: HomeComponent, pathMatch: 'full'},
//   {path: 'not-found', component: FourOhFourComponent},
//   {path: '**', redirectTo: 'not-found'},
// ];

const firebaseConfig = {
  apiKey: "AIzaSyB_EBZG7QVI6TXcufOGA7l23VbM-Y9sNIs",
  authDomain: "my-movie-pi.firebaseapp.com",
  projectId: "my-movie-pi",
  storageBucket: "my-movie-pi.appspot.com",
  messagingSenderId: "690751329830",
  appId: "1:690751329830:web:e42cdf9ba5f6096028b8e7",
  measurementId: "G-69M7TMBY6P",
  databaseURL: "https://my-movie-pi-default-rtdb.europe-west1.firebasedatabase.app/"

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
    SliderComponent,
    FooterComponent,
    RecommendationComponent,

  ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        BrowserAnimationsModule,
        HttpClientModule,
        FormsModule,
        PipeModule,
        CarouselModule,
        SidebarModule,
        MatProgressSpinnerModule,
        MatProgressBarModule,
        SkeletonModule,

        GenreModule,
        GenreListModule,
        MovieDetailsModule,
        MoviesModule,
        PersonModule,

        NgbModule,
        ReactiveFormsModule,
        // RouterModule.forRoot(appRoutes),
        FontAwesomeModule,
        AngularFireModule.initializeApp(firebaseConfig),
        AngularFirestoreModule,
        AngularFireAuthModule,
        provideFirebaseApp(() => initializeApp(environment.firebase)),
        // provideAnalytics(() => getAnalytics()),
        provideAuth(() => getAuth()),
        ButtonModule,
        // provideDatabase(() => getDatabase()),
        // provideFirestore(() => getFirestore()),
        // provideFunctions(() => getFunctions()),
        // provideMessaging(() => getMessaging()),
        // providePerformance(() => getPerformance()),
        // provideRemoteConfig(() => getRemoteConfig()),
        // provideStorage(() => getStorage()),
    ],
  providers: [AuthService, MoviesService, ScreenTrackingService, UserTrackingService,WindowRefService],
  bootstrap: [AppComponent]
})
export class AppModule {
}
