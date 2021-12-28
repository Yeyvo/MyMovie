import {Component, Input, OnDestroy, OnInit} from '@angular/core';
import {delay} from 'rxjs/internal/operators/delay';
import {MoviesService} from "../../services/movies.service";
import {Subscription} from "rxjs";

// import {Movie} from "../../models/Movie";

@Component({
  selector: 'app-movies',
  templateUrl: './movies.component.html',
  styleUrls: ['./movies.component.scss']
})
export class MoviesComponent implements OnInit, OnDestroy {
  topRated: any;
  responsiveOptions;
  loader = true;
  totalResults: any;
  total_results: number;
  searchRes: any = null;
  searchStr: string = "";
  isSearching: boolean = false;

  moviesSearchSubscription: Subscription;

  constructor(private movieService: MoviesService) {
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
    // if (!this.isSearching) {
      //this.getTopRatedMovies(1);
      this.getMovies();
    // }
    this.moviesSearchSubscription = this.movieService.moviesSearchSubject.subscribe(
      (movieSearchResult) => {
        this.searchRes = movieSearchResult;
        this.topRated = null;
        this.totalResults = this.movieService.searchlength;
        this.loader = false;
        this.isSearching = true;
      }
    );
    this.movieService.emitMovieSearch();
  }

  getTopRatedMovies(page: number) {
    this.movieService.getTopRatedMovies(page).pipe(delay(2000)).subscribe((res: any) => {
        this.topRated = res.results;
        this.totalResults = res.total_results;
        this.loader = false;
      },
      error => console.log(error));
  }

  changePage(event) {
    this.loader = true;
    if (this.isSearching) {
      this.movieService.searchMoviesPage(event.pageIndex + 1);
    } else {
      this.getTopRatedMovies(event.pageIndex + 1);
    }
  }

  // searchMovies() {
  //   // this.movieService.searchMovies(this.searchStr).subscribe(res => {
  //   //   this.searchRes = res.results;
  //   // });
  //   this.movieService.searchMovies(this.searchStr);
  // }

  getMovies(){
    this.getTopRatedMovies(1);
  }


  ngOnDestroy(): void {
    this.moviesSearchSubscription.unsubscribe();
  }



}
