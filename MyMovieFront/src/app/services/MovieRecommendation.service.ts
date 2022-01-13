import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class MovieRecommendationService {

  urlBase : string = 'http://127.0.0.1:4996';

  constructor(private httpClient : HttpClient) { }

  getRecomendation(): Observable<any>{
    return this.httpClient.get(this.urlBase+"/recomendation");
  }
}
