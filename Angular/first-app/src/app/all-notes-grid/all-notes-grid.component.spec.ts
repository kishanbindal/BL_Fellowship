import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AllNotesGridComponent } from './all-notes-grid.component';

describe('AllNotesGridComponent', () => {
  let component: AllNotesGridComponent;
  let fixture: ComponentFixture<AllNotesGridComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AllNotesGridComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AllNotesGridComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
