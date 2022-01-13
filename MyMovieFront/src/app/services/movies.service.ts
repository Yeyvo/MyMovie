import { Injectable } from '@angular/core';
import {Observable, Subject} from "rxjs";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})

export class MoviesService {
  baseUrl: string;
  apiKey: string;
  language: string;
  region: string;
  searchRes: any = null;

  moviesSearchSubject: Subject<any> = new Subject<any>();
  isMoviesSearchSubject: Subject<any> = new Subject<any>();
  searchlength: number = 0;
  searchStr: string;
  isSearching: boolean = false;

  constructor(private http: HttpClient) {
    this.baseUrl = 'https://api.themoviedb.org/3/';
    this.apiKey = '38822594572ba49838eb67eec9246d29';
    this.language = 'en-US';
    this.region = 'US';
  }

  emitMovieSearch() {
    this.moviesSearchSubject.next(this.searchRes);
  }

  emitIsMovieSearch() {
    this.isMoviesSearchSubject.next(this.isSearching);
  }

  getNowPlaying(page: number): Observable<any> {
    this.isSearching = false;
    this.emitIsMovieSearch();
    return this.http.get(`${this.baseUrl}movie/now_playing?api_key=${this.apiKey}&page=${page}&language=${this.language}&region=${this.region}`);
  }


  searchMovies(searchStr: string, page: number): any {
    this.searchStr = searchStr;
    this.isSearching = true;
    this.emitIsMovieSearch();
    console.log(`${this.baseUrl}search/movie?api_key=${this.apiKey}&query=${searchStr}`);
    this.http.get(`${this.baseUrl}search/movie?api_key=${this.apiKey}&query=${searchStr}&page=${page}`).subscribe((res: any) => {
      this.searchRes = res.results;
      this.searchlength = res.total_results;
      this.emitMovieSearch();
    });
  }

  getPopular(page: number): Observable<any> {
    this.isSearching = false;
    this.emitIsMovieSearch();
    return this.http.get(`${this.baseUrl}movie/popular?api_key=${this.apiKey}&page=${page}&language=${this.language}&region=${this.region}`);
  }

  getUpComingMovies(page: number): Observable<any> {
    this.isSearching = false;
    this.emitIsMovieSearch();
    return this.http.get(`${this.baseUrl}movie/upcoming?api_key=${this.apiKey}&page=${page}&language=${this.language}&region=${this.region}`);
  }

  getTopRatedMovies(page: number): Observable<any> {
    console.log(`${this.baseUrl}movie/top_rated?api_key=${this.apiKey}&page=${page}&language=${this.language}&region=${this.region}`)
    this.searchStr = "";
    this.isSearching = false;
    this.emitIsMovieSearch();
    this.searchRes = null;
    return this.http.get(`${this.baseUrl}movie/top_rated?api_key=${this.apiKey}&page=${page}&language=${this.language}&region=${this.region}`);
  }

  getDiscoverMovies(): Observable<any> {
    this.isSearching = false;
    return this.http.get(`${this.baseUrl}discover/movie?api_key=${this.apiKey}`);
  }

  getGenres(): Observable<any> {
    this.isSearching = false;
    this.emitIsMovieSearch();
    return this.http.get(`${this.baseUrl}genre/movie/list?api_key=${this.apiKey}&language=${this.language}`);
  }

  getMoviesByGenre(id: string): Observable<any> {
    this.isSearching = false;
    this.emitIsMovieSearch();
    return this.http.get(`${this.baseUrl}genre/${id}/movies?api_key=${this.apiKey}`);
  }

  getMovie(id: string): Observable<any> {
    this.isSearching = false;
    this.emitIsMovieSearch();
    return this.http.get(`${this.baseUrl}movie/${id}?api_key=${this.apiKey}`);
  }

  getMovieReviews(id: string): Observable<any> {
    this.isSearching = false;
    this.emitIsMovieSearch();
    return this.http.get(`${this.baseUrl}movie/${id}/reviews?api_key=${this.apiKey}`);
  }

  getMovieCredits(id: string): Observable<any> {
    this.isSearching = false;
    this.emitIsMovieSearch();
    return this.http.get(`${this.baseUrl}movie/${id}/credits?api_key=${this.apiKey}`);
  }

  getBackdropsImages(id: string) {
    this.isSearching = false;
    this.emitIsMovieSearch();
    return this.http.get(`${this.baseUrl}movie/${id}/images?api_key=${this.apiKey}`);
  }

  getMovieVideos(id: string): Observable<any> {
    this.isSearching = false;
    this.emitIsMovieSearch();
    return this.http.get(`${this.baseUrl}movie/${id}/videos?api_key=${this.apiKey}`);
  }

  getRecomendMovies(id: string): Observable<any> {
    this.isSearching = false;
    this.emitIsMovieSearch();
    return this.http.get(`${this.baseUrl}movie/${id}/recommendations?api_key=${this.apiKey}`);
  }

  getPersonDetail(id: string): Observable<any> {
    this.isSearching = false;
    this.emitIsMovieSearch();
    return this.http.get(`${this.baseUrl}person/${id}?api_key=${this.apiKey}`);
  }

  getPersonExternalData(id: string) {
    this.isSearching = false;
    this.emitIsMovieSearch();
    return this.http.get(`${this.baseUrl}person/${id}/external_ids?api_key=${this.apiKey}`);
  }

  getPersonCast(id: string): Observable<any> {
    this.isSearching = false;
    this.emitIsMovieSearch();
    return this.http.get(`${this.baseUrl}person/${id}/movie_credits?api_key=${this.apiKey}`);
  }
  searchMoviesPage(page: number) {
    this.searchMovies(this.searchStr, page);
  }
}
