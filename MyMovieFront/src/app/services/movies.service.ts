import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class MoviesService {
  baseUrl: string ;
  apiKey: string ;
  language: string ;
  region: string ;

  constructor() {
    this.baseUrl = 'https://api.themoviedb.org/3/';
    this.apiKey = 'dd4d819639705d332d531217b4f7c6b6';
    this.language = 'en-US';
    this.region = 'US';
  }
}
