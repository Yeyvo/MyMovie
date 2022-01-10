import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class CnnGenreService {

  urlBase : string = 'http://127.0.0.1:4996';

  constructor(private httpClient : HttpClient) { }

  getMovieGenre(posterId :string): Observable<any>{
    return this.httpClient.get(this.urlBase+"/categorization?posterId="+posterId.slice(1,posterId.length));
  }
}
