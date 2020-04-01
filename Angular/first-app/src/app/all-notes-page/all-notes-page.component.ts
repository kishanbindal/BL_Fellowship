import { Component, OnInit } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Component({
  selector: 'app-all-notes-page',
  templateUrl: './all-notes-page.component.html',
  styleUrls: ['./all-notes-page.component.css']
})
export class AllNotesPageComponent implements OnInit {

  // allNotes; 

  constructor() { 
  }

  view = false

  ngOnInit(): void {
    // this.recieveNotes()
    // console.log(this.allNotes)
    }
  
  getListSignal($event){
    console.log('Event in all notes grid Component : ', $event);
    this.view = $event;
  }
    
  // recieveNotes(){
  //   this.allNotesService.getAllNotes()
  //   let note_data = this.allNotesService.cast.subscribe((data) => {this.allNotes = data});
  //   setTimeout(()=> {console.log('All notes here : \n',this.allNotes)}, 5000)
  // }
}

