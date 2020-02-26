import { Component, OnInit } from '@angular/core';
import { AllNotesPageService } from '../services/allNotesPageService/all-notes-page-service.service';
import { Note } from '../note';

@Component({
  selector: 'app-all-notes-page',
  templateUrl: './all-notes-page.component.html',
  styleUrls: ['./all-notes-page.component.css']
})
export class AllNotesPageComponent implements OnInit {

  allNotes:Array<Note>;

  constructor(private allNotesService: AllNotesPageService) { 
  }

  ngOnInit(): void{
    this.recieveNotes('OnInit');
    console.log(this.allNotes)
  }

  recieveNotes(msg:string){
    this.allNotesService.getAllNotes().subscribe((response)=>this.allNotes)
    // console.log(request)
    // request.subscribe(response => {console.log(response)})
  }

}

