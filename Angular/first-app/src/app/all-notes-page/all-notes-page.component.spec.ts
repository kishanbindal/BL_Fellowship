import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AllNotesPageComponent } from './all-notes-page.component';

describe('AllNotesPageComponent', () => {
  let component: AllNotesPageComponent;
  let fixture: ComponentFixture<AllNotesPageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AllNotesPageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AllNotesPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
