import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import {MoviesService} from "../../services/movies.service";
import { delay } from 'rxjs/internal/operators/delay';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class HomeComponent implements OnInit {
  nowPlaying: any;
  tvShows: any;
  responsiveOptions;
  loader = true;

  constructor(
    private movies: MoviesService,
  ) {
    this.responsiveOptions = [
      {
        breakpoint: '1024px',
        numVisible: 3,
        numScroll: 3
      },
      {
        breakpoint: '768px',
        numVisible: 2,
        numScroll: 2
      },
      {
        breakpoint: '560px',
        numVisible: 1,
        numScroll: 1
      }
    ];
  }
  ngOnInit() {
    this.trendingMovies(1);
  }

  trendingMovies(page: number) {
    this.movies.getNowPlaying(page).pipe(delay(200)).subscribe((res: any) => {
      this.nowPlaying = res.results;
      this.loader = false;
    });
  }
}
