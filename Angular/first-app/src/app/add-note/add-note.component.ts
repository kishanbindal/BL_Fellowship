import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-add-note',
  templateUrl: './add-note.component.html',
  styleUrls: ['./add-note.component.css']
})
export class AddNoteComponent implements OnInit {

  showCard: boolean;

  templateNote: {
    collaborators: Array<string>,
    color: string,
    created_on: string,
    id: number,
    is_archived: boolean,
    is_pinned: boolean,
    is_trashed: boolean,
    labels: Array<string>,
    last_edited: string,
    link: string,
    note_image: File,
    note_text: string,
    reminder: string,
    title: string,
  }

  constructor() {
    this.showCard = false;
  }

  ngOnInit(): void {
  }

  openCard(){
    if (this.showCard === false){
      return this.showCard = true
    }
  }

  closeCard(){
    if(this.showCard === true){
      this.showCard = false;
      console.log(this.showCard);
      return this.showCard
    }
  }

}