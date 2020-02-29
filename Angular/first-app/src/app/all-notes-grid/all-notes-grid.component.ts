import { Component, OnInit } from '@angular/core';
import { AllNotesDataService } from '../services/allNotesDataService/all-notes-data-service.service';

@Component({
  selector: 'app-all-notes-grid',
  templateUrl: './all-notes-grid.component.html',
  styleUrls: ['./all-notes-grid.component.css']
})
export class AllNotesGridComponent implements OnInit {

  allNotes; 

  constructor(private allNotesService: AllNotesDataService) { }

  ngOnInit(): void {
    this.recieveNotes()
    // console.log(this.allNotes)
  }

  recieveNotes(){
    let recievedArray = []
    this.allNotesService.getAllNotes()
    this.allNotesService.cast.subscribe((data) => {this.allNotes = data});
  }
}
