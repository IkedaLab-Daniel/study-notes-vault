import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  data: [],
  loading: true,
};

export const charactersSlice = createSlice({
  name: 'characters',
  initialState,
  reducers: {
    add: (state, action) => {
      state.characters = action.payload;
    },
  },
});
