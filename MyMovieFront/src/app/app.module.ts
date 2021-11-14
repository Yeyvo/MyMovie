import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {FormsModule} from "@angular/forms";
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

const appRoutes: Routes = [
  {path: 'auth/signup', component: SignupComponent},
  {path: 'auth/signin', component: SigninComponent},
  // {path: 'movies',/*canActivate:[AuthGuardService], */component: },
  // {path: 'movies/view/:id',/*canActivate:[AuthGuardService], ,*/ component: SingleBookComponent},
  // {path: 'movies/new',/*canActivate:[AuthGuardService], ,*/ component: FormBookComponent},
  {path: '', component:HomeComponent, pathMatch: 'full'},
  {path: 'not-found', component: FourOhFourComponent},
  { path: '**' , redirectTo:'not-found'},
];

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
  ],
  providers: [AuthService, MoviesService],
  bootstrap: [AppComponent]
})
export class AppModule {
}
