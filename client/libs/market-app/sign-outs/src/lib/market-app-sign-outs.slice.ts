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
  reducers: {
    logout: (state) => {
      // From here we can take action only at this state
      // But, as we have taken care of this particular "logout" action
      // in rootReducer, we can use it to CLEAR the complete Redux Store's state
    },
  },
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

export const { logout } = signOutUserUpSlice.actions;
