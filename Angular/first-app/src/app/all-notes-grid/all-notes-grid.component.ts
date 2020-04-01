import { Component, OnInit, Input } from '@angular/core';
import { DataService } from '../services/DataService/data-service.service';


@Component({
  selector: 'app-all-notes-grid',
  templateUrl: './all-notes-grid.component.html',
  styleUrls: ['./all-notes-grid.component.css']
})
export class AllNotesGridComponent implements OnInit {

  allNotes; 
  @Input() view ;

  constructor(private allNotesService: DataService) { }

  ngOnInit(): void {
    this.recieveNotes()
    // console.log(this.allNotes)
  }

  recieveNotes(){
    this.allNotesService.getAllNotes()
    this.allNotesService.cast.subscribe((data) => {this.allNotes = data});
  }


}
