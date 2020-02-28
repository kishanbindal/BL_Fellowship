import { TestBed } from '@angular/core/testing';

import { AllNotesDataService } from './all-notes-data-service.service';

describe('AllNotesPageServiceService', () => {
  let service: AllNotesDataService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AllNotesDataService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
