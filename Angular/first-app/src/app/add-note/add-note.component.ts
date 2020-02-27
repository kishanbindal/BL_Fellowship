import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-add-note',
  templateUrl: './add-note.component.html',
  styleUrls: ['./add-note.component.css']
})
export class AddNoteComponent implements OnInit {

  showCard: boolean;

  constructor() {
    this.showCard = false;
  }

  ngOnInit(): void {
  }

  openCard(){
    if (this.showCard === false){
      return this.showCard = true
    }else{
      return this.showCard = false;
    }
  }

}

// Note Add Screen Dialog
