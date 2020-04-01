import { Component, OnInit, OnDestroy, Inject, OnChanges } from '@angular/core';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { DataService } from '../services/DataService/data-service.service';
import { FormControl, Validators } from '@angular/forms';
import { SingleCardDialogComponent } from '../single-card/single-card.component';

@Component({
  selector: 'app-label',
  templateUrl: './label.component.html',
  styleUrls: ['./label.component.css']
})
export class LabelComponent implements OnInit {

  labels


  constructor(public dialog: MatDialog, private dataService: DataService) {
    // this.dataService.getLabels();
    this.dataService.labelData.subscribe(result => {this.labels = result})
    console.log('Labels : ', this.labels)
   }

  ngOnInit(): void {
    
  }

  openLabelDialog(){
    console.log('Opening Dialog Box')
    const dialogRef = this.dialog.open(LabelDialogComponent,{
      // width: '30em', 
      maxHeight: "30em",
    })

    dialogRef.afterClosed().subscribe(result => {
      this.dataService.getLabels()
      this.dataService.labelData.subscribe(data => this.labels = data)
    })
  }
}


@Component({
  selector: 'app-label-dialog',
  templateUrl: './label-dialog.component.html',
  styleUrls: ['label-dialog.component.css']
})
export class LabelDialogComponent implements OnDestroy, OnInit{

  labels 

  showDeleteButton = false;

  label_name = new FormControl(null, [
    Validators.min(2)
  ])

  constructor(public dialogRef : MatDialogRef<SingleCardDialogComponent>,
    public dataService : DataService,
    @Inject(MAT_DIALOG_DATA) public data
    ){}

  ngOnInit(){
    // this.dataService.getLabels();
    this.dataService.labelData.subscribe(result => {this.labels = result})
    // console.log('coming from here')
  }
  
  ngOnDestroy(){
  }

  resetLabelInputData(){
    this.label_name = null;
    console.log(this.label_name);
  }

  getButton(){
    if(this.showDeleteButton === false){
      return this.showDeleteButton = true
    }
  }

  removeButton(){
    if(this.showDeleteButton === true){
      return this.showDeleteButton = false
    }
  }

  submitLabel(){
    console.log('Label Name : ', this.label_name.value);
    let label_data = {'label_name': this.label_name.value}
    if (this.label_name.value != null || this.label_name.value == ''){
      this.dataService.postLabel(label_data).subscribe(result => {
        console.log('Data in Submit Labels : ', result)
        if (result['success'] === true){
          this.dataService.getLabels()
          this.dataService.labelData.subscribe(data => this.labels = data)
          console.log('Labels after Submitting : ', this.labels)
          this.label_name = null;
        }
      })
    }  
  }

  deleteLabel(labelId: number){
    console.log('Label ID : ', labelId);
    this.dataService.deleteLabelId(labelId).subscribe(result => {
      if (result['success'] === true){
        this.dataService.getLabels()
        this.dataService.labelData.subscribe(data => this.labels = data)
      }
    })
  }

  updateLabel(label){
    this.dataService.updateLabelId(label).subscribe(response => {
      if (response['success']){
        this.dataService.getLabels()
        this.dataService.labelData.subscribe(data => this.labels = data)
      }
    })
  }

  // deleteLabel(label_id:number){
  //   this.dataService.deleteLabelId(label_id).subscribe(response => {
  //     console.log(response)
  //     if (response['success'] === true){
  //       this.dataService.getLabels()
  //       this.dataService.labelData.subscribe(data => this.labels = data)
  //     }
  //   })
  // }
}
