import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/DataService/data-service.service';

@Component({
  selector: 'app-archived-grid',
  templateUrl: './archived-grid.component.html',
  styleUrls: ['./archived-grid.component.css']
})
export class ArchivedGridComponent implements OnInit {

  archivedNotes;

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
    this.getArchived()
  }

  getArchived(){
    this.dataService.getArchivedNotes()
    this.dataService.archivedNotes.subscribe((data) => {console.log(data); this.archivedNotes = data})
    setTimeout(()=> console.log('Archived Notes : ', this.archivedNotes), 1000)
  }

}
