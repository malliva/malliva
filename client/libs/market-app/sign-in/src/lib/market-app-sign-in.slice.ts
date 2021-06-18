import { createSelector, createSlice, PayloadAction } from '@reduxjs/toolkit';

import { getSingInUser } from '@client/shared/account-syn-api';

export const USERS_KEY = 'signin';
type SignInError = any;
export const SIGNIN_USER_KEY = 'signin';

export const initialSignInState = {
  response: {},
  loading: 'idle',
  error: {},
};

export const signInSlice = createSlice({
  name: SIGNIN_USER_KEY,
  initialState: initialSignInState,
  reducers: {},
  //Thunk actions here
  extraReducers: (builder) => {
    builder.addCase(
      getSingInUser.pending,
      (state, action: PayloadAction<undefined>) => {
        state.loading = 'pending';
        state.response = [];
      }
    );
    builder.addCase(getSingInUser.fulfilled, (state, { payload }) => {
      state.response = payload.data;
      state.loading = 'succeeded';
      state.error = '';
    });
    builder.addCase(
      getSingInUser.rejected,
      (state, action: PayloadAction<SignInError>) => {
        state.error = action.payload.error;
        state.loading = 'failed';
      }
    );
  },
});
// Action creators are generated for each case reducer function
export const signInSliceReducer = signInSlice.reducer;

export const getSignInState = (stateObj: any) => stateObj[SIGNIN_USER_KEY];

export const selectSignInStateLoaded = createSelector(
  getSignInState,
  (stateObj) => stateObj
);
