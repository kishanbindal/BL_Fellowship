import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchNotesGridComponent } from './search-notes-grid.component';

describe('SearchNotesGridComponent', () => {
  let component: SearchNotesGridComponent;
  let fixture: ComponentFixture<SearchNotesGridComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SearchNotesGridComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchNotesGridComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
