import { createSlice, PayloadAction } from '@reduxjs/toolkit';

import { Error } from '@client/shared/account-syn-api';

export const USERS_KEY = 'signup';

export const SIGNUP_USER_KEY = 'signup';

export const initialSignInState = {
  response: [],
};

export const signUpSlice = createSlice({
  name: SIGNUP_USER_KEY,
  initialState: initialSignInState,
  reducers: {
    getSignUpUserDetails: (state, action) => {
      console.log(action);
    },
    getSignUpSuccess: (state, action: PayloadAction<any>) => {
      console.log(action);
    },
    getSignUpFailure: (state, action: PayloadAction<Error>) => {
      console.log(action);
    },
  },
});
// Action creators are generated for each case reducer function
export const {
  getSignUpUserDetails,
  getSignUpSuccess,
  getSignUpFailure,
} = signUpSlice.actions;

export default signUpSlice.reducer;
