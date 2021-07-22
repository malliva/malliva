import { createSelector, createSlice, PayloadAction } from '@reduxjs/toolkit';

import { postSingOutUser } from '@client/shared/account-syn-api';

export const USERS_KEY = 'logout';

export const SIGNOUT_USER_KEY = 'logout';

type SignOutUserError = any;

const initialSignOutUserState = {
  response: {},
  loading: 'idle',
  error: {},
};
export const signOutUserUpSlice = createSlice({
  name: SIGNOUT_USER_KEY,
  initialState: initialSignOutUserState,
  reducers: {},
  //Thunk actions here
  extraReducers: (builder) => {
    builder.addCase(
      postSingOutUser.pending,
      (state, action: PayloadAction<undefined>) => {
        state.loading = 'pending';
        state.response = [];
      }
    );
    builder.addCase(postSingOutUser.fulfilled, (state, { payload }) => {
      state.response = payload.data;
      state.loading = 'succeeded';
      state.error = '';
    });
    builder.addCase(
      postSingOutUser.rejected,
      (state, action: PayloadAction<SignOutUserError>) => {
        state.error = action.payload.error;
        state.loading = 'failed';
      }
    );
  },
});
// Action creators are generated for each case reducer function
export const signOutUserSliceReducer = signOutUserUpSlice.reducer;

export const signOutUsersState = (stateObj: any) => stateObj[SIGNOUT_USER_KEY];

export const selectSignOutStateStateLoaded = createSelector(
  signOutUsersState,
  (stateObj) => stateObj
);
