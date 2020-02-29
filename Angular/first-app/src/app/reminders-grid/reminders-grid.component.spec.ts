import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RemindersGridComponent } from './reminders-grid.component';

describe('RemindersGridComponent', () => {
  let component: RemindersGridComponent;
  let fixture: ComponentFixture<RemindersGridComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RemindersGridComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RemindersGridComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
