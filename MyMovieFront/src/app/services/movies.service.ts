import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class MoviesService {
  baseUrl: string = "https://api.themoviedb.org/3/";
  apiKey: string = "";
  language: string = "en-US";
  region: string = 'US';

  constructor() { }
}
