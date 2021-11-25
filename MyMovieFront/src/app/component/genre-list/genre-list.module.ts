import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';



import { GenreListRoutingModule } from './genre-list-routing.module';
import { GenreListComponent } from './genre-list.component';
import { SkeletonModule } from 'src/app/shared/skeleton/skeleton.module';
import {MatButtonModule} from "@angular/material/button";


@NgModule({
  declarations: [GenreListComponent],
  imports: [
    CommonModule,
    GenreListRoutingModule,
    MatButtonModule,
    SkeletonModule
  ]
})
export class GenreListModule { }
