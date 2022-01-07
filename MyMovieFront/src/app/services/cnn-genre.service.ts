import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class CnnGenreService {

  urlBase : string = '172.0.0.2';

  constructor(private httpClient : HttpClient) { }

  getMovieGenre(MovieURL :string): Observable<any>{
    return this.httpClient.get(this.urlBase+"/categorization?movieURL="+MovieURL);
  }
}
