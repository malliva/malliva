import { createSelector, createSlice, PayloadAction } from '@reduxjs/toolkit';

import { postSignUpUser } from '@client/shared/account-syn-api';

export const USERS_KEY = 'signup';

export const SIGNUP_USER_KEY = 'signup';

type SignUpError = any;

const initialSignUpState = {
  response: {},
  loading: 'idle',
  error: {},
};
export const signUpSlice = createSlice({
  name: SIGNUP_USER_KEY,
  initialState: initialSignUpState,
  reducers: {},
  //Thunk actions here
  extraReducers: (builder) => {
    builder.addCase(
      postSignUpUser.pending,
      (state, action: PayloadAction<undefined>) => {
        state.loading = 'pending';
        state.response = [];
      }
    );
    builder.addCase(postSignUpUser.fulfilled, (state, { payload }) => {
      state.response = payload.data;
      state.loading = 'succeeded';
      state.error = '';
    });
    builder.addCase(
      postSignUpUser.rejected,
      (state, action: PayloadAction<SignUpError>) => {
        state.error = action.payload.error;
        state.loading = 'failed';
      }
    );
  },
});
// Action creators are generated for each case reducer function
export const signUpSliceReducer = signUpSlice.reducer;

export const getsignUpState = (stateObj: any) => stateObj[SIGNUP_USER_KEY];

export const selectSignUpStateLoaded = createSelector(
  getsignUpState,
  (stateObj) => stateObj
);

export default signUpSlice.reducer;
