import { render } from '@testing-library/react';

import MarketAppToast from './market-app-toast';

describe('MarketAppToast', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<MarketAppToast />);
    expect(baseElement).toBeTruthy();
  });
});
