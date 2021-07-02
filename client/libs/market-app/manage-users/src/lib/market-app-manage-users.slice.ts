import { createSelector, createSlice, PayloadAction } from '@reduxjs/toolkit';

import { getRegisteredUsers } from '@client/shared/account-syn-api';

export const USERS_KEY = 'users';

export const REGISTERED_USER_KEY = 'users';

type REGISTEREDError = any;

const initialRegisteredUserState = {
  response: {},
  loading: 'idle',
  error: {},
};
export const registeredUserUpSlice = createSlice({
  name: REGISTERED_USER_KEY,
  initialState: initialRegisteredUserState,
  reducers: {},
  //Thunk actions here
  extraReducers: (builder) => {
    builder.addCase(
      getRegisteredUsers.pending,
      (state, action: PayloadAction<undefined>) => {
        state.loading = 'pending';
        state.response = [];
      }
    );
    builder.addCase(getRegisteredUsers.fulfilled, (state, { payload }) => {
      state.response = payload.data;
      state.loading = 'succeeded';
      state.error = '';
    });
    builder.addCase(
      getRegisteredUsers.rejected,
      (state, action: PayloadAction<REGISTEREDError>) => {
        state.error = action.payload.error;
        state.loading = 'failed';
      }
    );
  },
});
// Action creators are generated for each case reducer function
export const registeredUserSliceReducer = registeredUserUpSlice.reducer;

export const getRegisteredUsersState = (stateObj: any) =>
  stateObj[REGISTERED_USER_KEY];

export const selectRegisteredStateStateLoaded = createSelector(
  getRegisteredUsersState,
  (stateObj) => stateObj
);
