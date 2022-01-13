import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {HomeComponent} from "./component/home/home.component";
import {SignupComponent} from "./component/auth/signup/signup.component";
import {SigninComponent} from "./component/auth/signin/signin.component";
import {ProfileComponent} from "./component/profile/profile.component";
import {FourOhFourComponent} from "./component/four-oh-four/four-oh-four.component";
import {RecommendationComponent} from "./component/recommendation/recommendation.component";

const routes: Routes = [{
  path: '',
  component: HomeComponent,
},

  {
    path: 'recommendation', component: RecommendationComponent
  },

  {
    path: 'movies',
    loadChildren: () => import('./component/movies/movies.module').then(mod => mod.MoviesModule)
  },

  {
    path: 'movies/:id',
    loadChildren: () => import('./component/movie-details/movie-details.module').then(mod => mod.MovieDetailsModule)
  },

  {
    path: 'genres/:id/:name',
    loadChildren: () => import('./component/genre/genre.module').then(mod => mod.GenreModule)
  },

  {
    path: 'genres',
    loadChildren: () => import('./component/genre-list/genre-list.module').then(mod => mod.GenreListModule)
  },

  {
    path: 'person/:id',
    loadChildren: () => import('./component/person/person.module').then(mod => mod.PersonModule)
  },
  {
    path: 'auth/signup', component: SignupComponent
  },
  {
    path: 'auth/signin', component: SigninComponent
  },
  {
    path: 'auth/profile', component: ProfileComponent
  },
  {
    path: 'not-found', component: FourOhFourComponent
  },
  {
    path: '**',
    redirectTo: 'not-found'
  },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
