import { Injectable } from '@angular/core';
import {Observable, Subject} from "rxjs";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
/**
 * Code from
 *
 * https://github.com/abidakram01/angular-movie-app/blob/e7674acb9ee0071ff303608efa06c59ea729ad4f/src/app/service/movies.service.ts
 */


export class MoviesService {
  baseUrl: string ;
  apiKey: string ;
  language: string ;
  region: string ;
  searchRes: any = null;

  moviesSearchSubject : Subject<any> = new Subject<any>();
  searchlength: number = 0;
  searchStr: string;

  constructor(private http : HttpClient) {
    this.baseUrl = 'https://api.themoviedb.org/3/';
    this.apiKey = '38822594572ba49838eb67eec9246d29';
    this.language = 'en-US';
    this.region = 'US';
  }

  emitMovieSearch() {
    this.moviesSearchSubject.next(this.searchRes);
  }

  getNowPlaying(page: number): Observable<any> {
    return this.http.get(`${this.baseUrl}movie/now_playing?api_key=${this.apiKey}&page=${page}&language=${this.language}&region=${this.region}`);
  }

  searchMovies(searchStr: string, page :number): any {
    this.searchStr = searchStr;
    console.log(`${this.baseUrl}search/movie?api_key=${this.apiKey}&query=${searchStr}`);
     this.http.get(`${this.baseUrl}search/movie?api_key=${this.apiKey}&query=${searchStr}&page=${page}`).subscribe((res: any) => {
       this.searchRes = res.results;
       this.searchlength = res.total_results;
       this.emitMovieSearch();
     });
  }

  getPopular(page: number): Observable<any> {
    return this.http.get(`${this.baseUrl}movie/popular?api_key=${this.apiKey}&page=${page}&language=${this.language}&region=${this.region}`);
  }

  getUpComingMovies(page: number): Observable<any> {
    return this.http.get(`${this.baseUrl}movie/upcoming?api_key=${this.apiKey}&page=${page}&language=${this.language}&region=${this.region}`);
  }

  getTopRatedMovies(page: number): Observable<any> {
    console.log(`${this.baseUrl}movie/top_rated?api_key=${this.apiKey}&page=${page}&language=${this.language}&region=${this.region}`)
    return this.http.get(`${this.baseUrl}movie/top_rated?api_key=${this.apiKey}&page=${page}&language=${this.language}&region=${this.region}`);
  }

  getDiscoverMovies(): Observable<any> {
    return this.http.get(`${this.baseUrl}discover/movie?api_key=${this.apiKey}`);
  }

  getGenres(): Observable<any> {
    return this.http.get(`${this.baseUrl}genre/movie/list?api_key=${this.apiKey}&language=${this.language}`);
  }

  getMoviesByGenre(id: string): Observable<any> {
    return this.http.get(`${this.baseUrl}genre/${id}/movies?api_key=${this.apiKey}`);
  }

  getMovie(id: string): Observable<any> {
    return this.http.get(`${this.baseUrl}movie/${id}?api_key=${this.apiKey}`);
  }

  getMovieReviews(id: string): Observable<any> {
    return this.http.get(`${this.baseUrl}movie/${id}/reviews?api_key=${this.apiKey}`);
  }

  getMovieCredits(id: string): Observable<any> {
    return this.http.get(`${this.baseUrl}movie/${id}/credits?api_key=${this.apiKey}`);
  }

  getBackdropsImages(id: string) {
    return this.http.get(`${this.baseUrl}movie/${id}/images?api_key=${this.apiKey}`);
  }

  getMovieVideos(id: string): Observable<any> {
    return this.http.get(`${this.baseUrl}movie/${id}/videos?api_key=${this.apiKey}`);
  }

  getRecomendMovies(id: string): Observable<any> {
    return this.http.get(`${this.baseUrl}movie/${id}/recommendations?api_key=${this.apiKey}`);
  }

  getPersonDetail(id: string): Observable<any> {
    return this.http.get(`${this.baseUrl}person/${id}?api_key=${this.apiKey}`);
  }

  getPersonExternalData(id: string) {
    return this.http.get(`${this.baseUrl}person/${id}/external_ids?api_key=${this.apiKey}`);
  }

  getPersonCast(id: string): Observable<any> {
    return this.http.get(`${this.baseUrl}person/${id}/movie_credits?api_key=${this.apiKey}`);
  }

  searchMoviesPage(page: number) {
    this.searchMovies(this.searchStr, page);
  }
}
