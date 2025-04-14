import { Component, OnInit } from '@angular/core';
import { IndexService } from './index.service';
import { IndexData } from './index.model';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.css']
})
export class IndexComponent implements OnInit {
  diaries: IndexData[] = [];
  isLoading = true;

  constructor(private indexService: IndexService) { }

  ngOnInit(): void {
    this.loadDiaries();
  }

  loadDiaries(): void {
    this.isLoading = true;
    this.indexService.getPublicDiaries().subscribe(
      diaries => {
        this.diaries = diaries;
        this.isLoading = false;
      },
      error => {
        console.error('Error loading diaries:', error);
        this.isLoading = false;
      }
    );
  }
}
