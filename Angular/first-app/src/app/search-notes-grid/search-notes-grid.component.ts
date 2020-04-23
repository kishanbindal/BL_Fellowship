import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/DataService/data-service.service';

@Component({
  selector: 'app-search-notes-grid',
  templateUrl: './search-notes-grid.component.html',
  styleUrls: ['./search-notes-grid.component.css']
})
export class SearchNotesGridComponent implements OnInit {

  searchedNotes

  constructor(private dataService: DataService) { 
  }

  ngOnInit(): void {
    this.dataService.searchNotes.subscribe(data => {
      // for(let i=0; i < data.length; i++){
      //   let tempData = data[i][0]
      //   console.log(tempData)
      //   this.searchedNotes.push(tempData)
      // }
      this.searchedNotes = data
      console.log('searched note data:',this.searchedNotes)
    })
  }

}
