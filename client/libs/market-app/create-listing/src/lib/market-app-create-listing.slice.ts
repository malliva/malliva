import { createSelector, createSlice, PayloadAction } from '@reduxjs/toolkit';

import { postCreateListing } from '@client/shared/account-syn-api';

export const CREATE_LISTINGS_KEY = 'listings';

type CreateListingError = any;

export const initialCreateListingState = {
  response: {},
  loading: 'idle',
  error: {},
};

export const createListingSlice = createSlice({
  name: CREATE_LISTINGS_KEY,
  initialState: initialCreateListingState,
  reducers: {},
  //Thunk actions here
  extraReducers: (builder) => {
    builder.addCase(
      postCreateListing.pending,
      (state, action: PayloadAction<undefined>) => {
        state.loading = 'pending';
        state.response = [];
      }
    );
    builder.addCase(postCreateListing.fulfilled, (state, { payload }) => {
      state.response = payload.data;
      state.loading = 'succeeded';
      state.error = '';
    });
    builder.addCase(
      postCreateListing.rejected,
      (state, action: PayloadAction<CreateListingError>) => {
        state.error = action.payload.error;
        state.loading = 'failed';
      }
    );
  },
});
// Action creators are generated for each case reducer function
export const createListingSliceReducer = createListingSlice.reducer;

export const getCreatedListingState = (stateObj: any) =>
  stateObj[CREATE_LISTINGS_KEY];

export const selectListingStateLoaded = createSelector(
  getCreatedListingState,
  (stateObj) => stateObj
);
