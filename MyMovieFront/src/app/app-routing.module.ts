import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {HomeComponent} from "./component/home/home.component";

const routes: Routes = [{
  path: '',
  component: HomeComponent,
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
    path: '**',
    redirectTo: ''
  }];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
