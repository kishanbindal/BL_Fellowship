import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ListviewGridviewComponent } from './listview-gridview.component';

describe('ListviewGridviewComponent', () => {
  let component: ListviewGridviewComponent;
  let fixture: ComponentFixture<ListviewGridviewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ListviewGridviewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ListviewGridviewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
