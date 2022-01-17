import {Component, OnDestroy, OnInit} from '@angular/core';
import {AuthService} from "../../services/auth.service";
import {User} from "../../models/User";
import {forkJoin, Subscription} from "rxjs";
import {MoviesService} from "../../services/movies.service";

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit,OnDestroy {
  private userSub: Subscription;
  user: User;
  recMovies: any[] = [];
  responsiveOptions = [
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
  hasRecommendations: boolean = false;
  scrollvalue: number;
  maxVisible: number;
  loader: boolean = true;


  constructor(public userAuth : AuthService,public movies : MoviesService) { }

  ngOnInit(): void {
    this.userSub = this.userAuth.user$.subscribe((data) => {
      this.user = data;
      let len = data.recommendedMovies.length;
      if(len>0){
        let factor = 1
        switch (len) {
          case 1:
            factor = 4;
            break;
          case 2:
            factor = 2
            break;
        }

        let obs  = []
        for (const recommended of data.recommendedMovies) {
          for (let i = 0; i < factor; i++) {
            obs.push(this.movies.getMovie(recommended));
          }
        }
        forkJoin(obs).subscribe((res)=>{
          this.recMovies = res;
          this.hasRecommendations = true;
          this.loader = false;
        })
      } else{
        this.loader = false;
      }
    });
  }

  ngOnDestroy(): void {
    this.userSub.unsubscribe();
  }

}
