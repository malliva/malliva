import { createSelector } from 'reselect';
import { ThunkAction } from 'redux-thunk';
import { createAsyncThunk, createSlice, PayloadAction } from '@reduxjs/toolkit';

import { getSingInUser, SignInState } from '@client/shared/account-syn-api';

export const USERS_KEY = 'signin';

export const SIGNIN_USER_KEY = 'signin';

export const initialSignInState: SignInState = {
  login: {
    email: '',
    password: '',
  },
  token: '',
  authorised: false,
  error: null,
};

export const signInSlice = createSlice({
  name: SIGNIN_USER_KEY,
  initialState: initialSignInState as SignInState,
  reducers: {
    getSignInUserDetails: (state, action: PayloadAction<undefined>) => {
      //   state.authorised = false;
      //   state.users.token = '';
      console.log(state);
    },
  },
  //Thunk actions here
  extraReducers: {
    [getSingInUser.fulfilled.type]: (state, action) => {
      console.log(state);
      //state.myAsyncResponse = action.payload;
    },
  },
});
// Action creators are generated for each case reducer function
export const { getSignInUserDetails } = signInSlice.actions;

export default signInSlice.reducer;

// Define a thunk that dispatches those action creators
export const dispatchSignInUser = (login) => async (dispatch) => {
  dispatch(getSingInUser(login));
};
