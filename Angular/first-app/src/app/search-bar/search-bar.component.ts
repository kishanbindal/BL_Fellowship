import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { DataService } from '../services/DataService/data-service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})
export class SearchBarComponent implements OnInit {
  
  constructor(private dataService: DataService,
    ) { }

  searchText = new FormControl('')

  ngOnInit(): void {

  }

  submitSearch(){
    let searchData = {'title': this.searchText.value}
    this.dataService.getSearchedNote(searchData)
  }

}
